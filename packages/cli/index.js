#!/usr/bin/env node

require = require('esm')(module /*, options*/)
require('./src/cli').default(process.argv.slice(2))