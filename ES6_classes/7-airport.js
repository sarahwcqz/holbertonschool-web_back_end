export default class Airport {
    constructor(name, code) {
        if (typeof name !== "string") {
        throw new TypeError("name must be a string");
        }
        if (typeof code !== "string") {
        throw new TypeError("code must be a string");
        }

        this._name = name;
        this._code = code;
        this[Symbol.toStringTag] = code;
    }

    get name() {
        return this._name;
    }

    get code() {
        return this._code;
    }
}
