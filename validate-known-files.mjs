#!/usr/bin/env node
// Validate known shared JSON files on disk against screenplan-contracts schemas.
// Usage: node packages/screenplan-contracts/validate-known-files.mjs
//
// Runs against any of the optional files below that exist locally; missing
// files are skipped (this script is also safe to run in CI on a fresh clone).

import * as fs from 'node:fs';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..', '..');

const TS_PKG = path.resolve(ROOT, 'packages', 'screenplan-contracts-ts');
const distIndex = path.join(TS_PKG, 'dist', 'index.js');
if (!fs.existsSync(distIndex)) {
  console.error(`screenplan-contracts-ts not built. Run: (cd ${TS_PKG} && npm run build)`);
  process.exit(2);
}

const {
  validateScriptStatus,
  validateEventStatus,
  validateScriptActionLog,
} = await import(distIndex);

const SEC_TMP = path.resolve(ROOT, 'components', 'Script-Engine-Controller', 'tmp');

const arrayCases = [
  { file: path.join(SEC_TMP, 'running_scripts.json'),   validator: validateScriptStatus, label: 'running_scripts'   },
  { file: path.join(SEC_TMP, 'completed_scripts.json'), validator: validateScriptStatus, label: 'completed_scripts' },
  { file: path.join(SEC_TMP, 'running_events.json'),    validator: validateEventStatus,  label: 'running_events'    },
  { file: path.join(SEC_TMP, 'completed_events.json'),  validator: validateEventStatus,  label: 'completed_events'  },
];

let total = 0;
let failures = 0;

for (const { file, validator, label } of arrayCases) {
  if (!fs.existsSync(file)) {
    console.log(`  skip  ${label} (no file at ${file})`);
    continue;
  }
  const items = JSON.parse(fs.readFileSync(file, 'utf8'));
  if (!Array.isArray(items)) {
    console.error(`  FAIL  ${label}: not an array`);
    failures += 1;
    continue;
  }
  let bad = 0;
  for (const [i, item] of items.entries()) {
    total += 1;
    try { validator.assert(item); }
    catch (err) {
      bad += 1;
      if (bad <= 3) console.error(`  FAIL  ${label}[${i}]: ${err.message}`);
    }
  }
  failures += bad;
  console.log(`  ${bad === 0 ? 'OK   ' : 'FAIL '} ${label} (${items.length - bad}/${items.length} valid)`);
}

// Optionally walk a logs/ dir and validate every action-log.json found
const logsDir = process.argv[2];
if (logsDir && fs.existsSync(logsDir)) {
  console.log(`\nWalking ${logsDir} for action-log.json files...`);
  const stack = [logsDir];
  while (stack.length) {
    const cur = stack.pop();
    for (const ent of fs.readdirSync(cur, { withFileTypes: true })) {
      const p = path.join(cur, ent.name);
      if (ent.isDirectory()) stack.push(p);
      else if (ent.name.endsWith('action-log.json')) {
        total += 1;
        try {
          validateScriptActionLog.assert(JSON.parse(fs.readFileSync(p, 'utf8')));
        } catch (err) {
          failures += 1;
          if (failures <= 5) console.error(`  FAIL  ${p}: ${err.message}`);
        }
      }
    }
  }
}

console.log(`\nValidated ${total} item(s); ${failures} failure(s).`);
process.exit(failures === 0 ? 0 : 1);
