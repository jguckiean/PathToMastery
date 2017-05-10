let secondMethodToCallFirstAsync = (() => {
    var _ref = _asyncToGenerator(function* () {
        var c = yield firstMethod();
    });

    return function secondMethodToCallFirstAsync() {
        return _ref.apply(this, arguments);
    };
})();
const b =(key, arg) => {
                try {
                    var info = gen[key](arg); 
                    var value = info.value;
                }
                catch (error) {
                    reject(error);
                    return;
                }
                if (info.done) {
                    resolve(value);
                }
                else {
                    return Promise.resolve(value)
                        .then(function (value) {
                            step("next", value);
                        },
                        function (err) {
                            step("throw", err);
                        });
                }
            }
const a =  (fn) => {
        var gen = fn.apply(this, arguments);
        return new Promise((resolve, reject) => {
            step = b;
            return step("next");
        });
    };


function _asyncToGenerator(fn) {
    return a(fn);
}

const firstMethod = () => "siddhant";