(function () {
    'use strict';

    angular
        .module('app')
        .controller('FriendController', FriendController);

    FriendController.$inject = ['UserService', '$rootScope','$location', '$scope'];
    function FriendController(UserService, $rootScope, $location) {
        var vm = this;

        vm.user = null;
        vm.allUsers = [];
        vm.deleteUser = deleteUser;
        vm.allUsersLen = 0;

        initController();


        function initController() {
            loadCurrentUser();
            loadAllUsers();
        }


        function loadCurrentUser() {
            UserService.GetByUsername($rootScope.globals.currentUser.username)
                .then(function (user) {
                    vm.user = user['person'][0];
                    var getpost = JSON.stringify({'user_id_a':user['person'][0].username,'user_id_b':$location.url().split('#')[1]});
                    loadPosts(getpost);
                    requestexists(user['person'][0].username);
                    requestexists2(user['person'][0].username);
                });
        }

        function loadAllUsers() {
            UserService.GetAll()
                .then(function (users) {
                    vm.allUsers = users['person'];
                    console.log(vm.allUsers);
                    if (vm.allUsers.length !== 0){
                        vm.allUsersLen = 1;
                    }
                    else{
                        vm.allUsersLen = 0;
                    }
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