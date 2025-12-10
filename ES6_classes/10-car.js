const _constructor = Symbol('constructor');

export default class Car {
    constructor(brand, motor, color) {
        if (typeof brand !== "string") throw new TypeError("brand must be a string");
        if (typeof motor !== "string") throw new TypeError("motor must be a string");
        if (typeof color !== "string") throw new TypeError("color must be a string");

        this._brand = brand;
        this._motor = motor;
        this._color = color;

        this[_constructor] = this.constructor;
    }

    get brand() { return this._brand; }
    get motor() { return this._motor; }
    get color() { return this._color; }

    cloneCar() {
        return new this[_constructor](this._brand, this._motor, this._color);
    }
}
