const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', () => {
  describe('SUM', () => {
    it('adds two integers', () => {
      expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    });

    it('rounds each number before the sum', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
  });

  describe('SUBTRACT', () => {
    it('subtracts b from a', () => {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('depends on the order of a and b', () => {
      expect(calculateNumber('SUBTRACT', 4.5, 1.4)).to.equal(4);
    });
  });

  describe('DIVIDE', () => {
    it('does not round the result', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('rounds a negative .5 toward positive infinity', () => {
      expect(calculateNumber('DIVIDE', -4.5, 2)).to.equal(-2);
    });

    it('returns Error when b is 0', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('returns Error when b rounds to 0', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0.4)).to.equal('Error');
    });

    it('returns Error when b rounds to -0', () => {
      expect(calculateNumber('DIVIDE', 1.4, -0.4)).to.equal('Error');
    });

    it('does not return Error when b rounds to 1', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0.5)).to.equal(1);
    });
  });
});
