const crypto = require('crypto');

class PicpikSigner {
  constructor(publicKey = "", privateKey = "", apiKey = "") {
    this.publicKey = publicKey;
    this.privateKey = privateKey;
    this.apiKey = apiKey;
  }

  _mapToString(params, exclusiveKey = null, strLimit = null) {
    let content = [];
    for (const key of this._extractSortedKeys(params)) {
      if (!exclusiveKey || exclusiveKey !== key) {
        content.push(`${key}${this._anyToString(params[key], strLimit)}`);
      }
    }
    return content.join("");
  }

  _anyToString(value, strLimit = null) {
    if (typeof value === "boolean") {
      return this._simpleToString(value).toLowerCase();
    } else if (typeof value === "number" && Number.isInteger(value)) {
      return this._simpleToString(value);
    } else if (typeof value === "object" && !Array.isArray(value)) {
      return this._mapToString(value);
    } else if (Array.isArray(value)) {
      return this._sliceToString(value, strLimit);
    } else if (typeof value === "string") {
      return this._formatString(value, strLimit);
    } else {
      return this._simpleToString(value);
    }
  }

  _sliceToString(arr, strLimit) {
    return arr.map(v => this._anyToString(v, strLimit)).join("");
  }

  _simpleToString(value) {
    if (value === null || value === "") {
      return "";
    }
    return String(value);
  }

  _formatString(value, limit) {
    if (limit && value.length > limit) {
      return value.substring(0, limit);
    }
    return value;
  }

  _extractSortedKeys(obj) {
    return Object.keys(obj).sort();
  }

  signService(body) {
    const content = this._mapToString(body, "signature", 128) + this.apiKey;
    const md5 = crypto.createHash('md5').update(content, 'utf-8').digest('hex');
    return md5;
  }

  signPlatform(body) {
    const content = this._mapToString(body) + this.privateKey;
    const sha1 = crypto.createHash('sha1').update(content, 'utf-8').digest('hex');
    return sha1;
  }
}

module.exports = PicpikSigner;
