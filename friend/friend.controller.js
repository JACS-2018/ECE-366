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
        vm.find = find;
        vm.searching = 0;
        vm.person = null;
        vm.exists = 0;
        vm.find2 = find2;

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
                });
        }

        function find(username) {
             if (typeof username !== 'undefined'){
                if(username.length !== 0){
                    vm.searching = 1;
                    UserService.GetByUsername(username)
                        .then(function (user) {
                            vm.person = user['person'];
                            if (vm.person.length !== 0){
                                vm.exists = 1;
                            }
                            else{
                                vm.exists = 0;
                            }
                        });
                }
                else{
                    vm.searching = 0;
                }
            }
            else{
                vm.searching = 0;
            }
            
        }

        function find2(){
            vm.searching = 0;
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