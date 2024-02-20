class window {
    constructor() {
      this._data = {};
    }
  
    __getattr__(name) {
      return this._data.get(name);
    }
  
    __setattr__(name, value) {
      this._data[name] = value;
    }
  
  }
  
  class Dataset {
    constructor(element) {
      this.element = element;
    }
  
    __getattr__(name) {
      return this.element.getAttribute("data-" + name);
    }
  
    __setattr__(name, value) {
      this.element.setAttribute("data-" + name, value);
    }
  
  }
  
  class Element {
    constructor(tag) {
      this.tag = tag;
      this.children = [];
      this.dataset = new Dataset(this);
      this.attributes = {};
    }
  
    appendChild(element) {
      this.children.append(element);
    }
  
    setAttribute(name, value) {
      this.attributes[name] = value;
    }
  
    getAttribute(name) {
      return this.attributes.get(name);
    }
  
  }
  
  class Document {
    constructor() {
      this._data = {};
      this._id = {};
    }
  
    __getattr__(name) {
      return this._data.get(name);
    }
  
    __setattr__(name, value) {
      this._data[name] = value;
    }
  
    createElement(tag, id) {
      this._data[id] = tag;
      this._id[id] = new Element(tag);
      return this._data.get(id);
    }
  
    getElementById(element_id) {
      return this._id.get(element_id);
    }
  
  }
  