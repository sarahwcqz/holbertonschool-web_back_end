const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const url = 'http://localhost:7865';

  it('returns status code 200', (done) => {
    request(url, (error, response) => {
      if (error) return done(error);
      expect(response.statusCode).to.equal(200);
      return done();
    });
  });

  it('returns the welcome message', (done) => {
    request(url, (error, response, body) => {
      if (error) return done(error);
      expect(body).to.equal('Welcome to the payment system');
      return done();
    });
  });

  it('returns an HTML content type', (done) => {
    request(url, (error, response) => {
      if (error) return done(error);
      expect(response.headers['content-type']).to.equal('text/html; charset=utf-8');
      return done();
    });
  });
});

describe('Cart page', () => {
  const url = 'http://localhost:7865/cart';

  it('returns status code 200 when :id is a number', (done) => {
    request(`${url}/12`, (error, response) => {
      if (error) return done(error);
      expect(response.statusCode).to.equal(200);
      return done();
    });
  });

  it('returns the payment methods message for the cart', (done) => {
    request(`${url}/12`, (error, response, body) => {
      if (error) return done(error);
      expect(body).to.equal('Payment methods for cart 12');
      return done();
    });
  });

  it('returns status code 404 when :id is NOT a number', (done) => {
    request(`${url}/hello`, (error, response) => {
      if (error) return done(error);
      expect(response.statusCode).to.equal(404);
      return done();
    });
  });

  it('returns status code 404 when :id is negative', (done) => {
    request(`${url}/-12`, (error, response) => {
      if (error) return done(error);
      expect(response.statusCode).to.equal(404);
      return done();
    });
  });

  it('returns status code 404 when :id is a decimal', (done) => {
    request(`${url}/12.5`, (error, response) => {
      if (error) return done(error);
      expect(response.statusCode).to.equal(404);
      return done();
    });
  });
});
