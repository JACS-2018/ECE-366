﻿(function () {
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

        function post(content) {
            if (typeof content !== 'undefined'){
                if(content.length !== 0){
                    content = content.trim();
                    var newpost = JSON.stringify({'user_id_a':vm.user.username,'user_id_b':vm.user.username, 'content':content});
                    console.log(content);
                     UserService.MakePost(newpost)
                        .then(function (posting) {
                            console.log(posting);
                            console.log(vm.user.username);
                            loadPosts(vm.user.username);
                        });
                }
            }
        }

        function loadCurrentUser() {
            UserService.GetByUsername($rootScope.globals.currentUser.username)
                .then(function (user) {
                    vm.user = user['person'][0];
                    console.log(user['person'][0].id)
                    loadPosts(user['person'][0].username);
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

        function loadPosts(userName) {
            UserService.GetPostById(userName)
                .then(function (posting) {
                    vm.allPosts = posting['posts'];
                    console.log(vm.allPosts);

                });
        }
    }

})();