const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('adds two integers', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('rounds b only', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('rounds a down and b up', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('rounds .5 up', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('rounds .5 up on an even number', () => {
    assert.strictEqual(calculateNumber(2.5, 0), 3);
  });

  it('rounds down just below .5', () => {
    assert.strictEqual(calculateNumber(1.4999, 0), 1);
  });

  it('rounds each number before the sum', () => {
    assert.strictEqual(calculateNumber(1.4, 1.4), 2);
  });

  it('rounds negative numbers', () => {
    assert.strictEqual(calculateNumber(-1.4, -1.6), -3);
  });

  it('rounds negative .5 toward positive infinity', () => {
    assert.strictEqual(calculateNumber(-1.5, 0), -1);
  });

  it('adds two zeros', () => {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });
});
