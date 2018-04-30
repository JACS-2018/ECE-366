(function () {
    'use strict';

    angular
        .module('app')
        .controller('HomeController', HomeController);

    HomeController.$inject = ['UserService', '$rootScope','$location', '$scope'];
    function HomeController(UserService, $rootScope) {
        var vm = this;

        vm.user = null;
        vm.allUsers = [];
        vm.deleteUser = deleteUser;
        vm.allPosts= [];
        vm.post = post;

        initController();

        function initController() {
            loadCurrentUser();
            loadAllUsers();
        }

        function post() {
            console.log(vm.post.content);
        }

        function loadCurrentUser() {
            UserService.GetByUsername($rootScope.globals.currentUser.username)
                .then(function (user) {
                    vm.user = user['person'][0];
                    console.log(user['person'][0].id)
                    loadPosts(user['person'][0].id);
                });
        }

         function loadUser(id) {
            UserService.GetByUsername(id)
                .then(function (user) {
                    console.log( user['person'][0].firstName + ' ' + user['person'][0].lastName);
                });
        }

        function loadAllUsers() {
            UserService.GetAll()
                .then(function (users) {
                    vm.allUsers = users['person'];
                });
        }

        function deleteUser(id) {
            UserService.Delete(id)
            .then(function () {
                loadAllUsers();
            });
        }

        function loadPosts(id) {
            UserService.GetPostById(id)
                .then(function (posting) {
                    vm.allPosts = posting['posts'];
                    console.log(vm.allPosts);
                });
        }
    }

})();