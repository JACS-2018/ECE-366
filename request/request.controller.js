(function () {
    'use strict';

    angular
        .module('app')
        .controller('RequestController', RequestController);

    RequestController.$inject = ['UserService', '$rootScope','$location'];
    function RequestController(UserService, $rootScope) {
        var vm = this;

        vm.user = null;
        vm.allUsers = [];
        vm.deleteUser = deleteUser;
        vm.changePage=changePage;

        initController();

        function initController() {
            loadCurrentUser();
            loadAllUsers();
        }

        function changePage(path){
            $location.path(path);
            console.log(path);
            console.log("hello");
        }

        function loadCurrentUser() {
            UserService.GetByUsername($rootScope.globals.currentUser.username)
                .then(function (user) {
                    vm.user = user;
                });
        }

        function loadAllUsers() {
            UserService.GetAll()
                .then(function (users) {
                    vm.allUsers = users['person'];
                    console.log(users['person']);
                });
        }

        function deleteUser(id) {
            UserService.Delete(id)
            .then(function () {
                loadAllUsers();
            });
        }
    }

})();