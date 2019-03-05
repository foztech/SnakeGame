
"use strict";

const _ = require('lodash');


class Apple {
    constructor(options) {
        _.assign(this, options);
        this.respawn();
    }

    respawn() {
        this.x = Math.random() * this.gridSize | 0;
        this.y = Math.random() * this.gridSize | 0;

        this._checkCollisions();

        return this;
    }

    _checkCollisions() {

        this.snakes.forEach((s) => {

            if(s.x === this.x && s.y === this.y) {
            this.respawn();
        }

        s.tail.forEach((t) => {
            if(t.x === this.x && t.y === this.y) {
            this.respawn();
        }
    });
    });

        this.apples.forEach((a) => {

            if(this !== a) {
            if(a.x === this.x && a.y === this.y) {
                this.respawn();
            }
        }
    });
    }
}

module.exports = Apple;
