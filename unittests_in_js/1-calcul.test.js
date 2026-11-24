const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
  describe('SUM', () => {
    it('adds two integers', () => {
      assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    });

    it('rounds each number before the sum', () => {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
  });

  describe('SUBTRACT', () => {
    it('subtracts b from a', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('depends on the order of a and b', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 4.5, 1.4), 4);
    });
  });

  describe('DIVIDE', () => {
    it('does not round the result', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('rounds a negative .5 toward positive infinity', () => {
      assert.strictEqual(calculateNumber('DIVIDE', -4.5, 2), -2);
    });

    it('returns Error when b is 0', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('returns Error when b rounds to 0', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.4), 'Error');
    });

    it('returns Error when b rounds to -0', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, -0.4), 'Error');
    });

    it('does not return Error when b rounds to 1', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.5), 1);
    });
  });
});
