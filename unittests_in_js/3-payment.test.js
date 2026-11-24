const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./3-payment.js');

describe('sendPaymentRequestToApi', () => {
  it('uses Utils.calculateNumber to compute the total', () => {
    const spy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);
    spy.restore();

    expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.equal(true);
    expect(spy.returnValues[0]).to.equal(Utils.calculateNumber('SUM', 100, 20));
  });
});
