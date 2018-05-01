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
        vm.areFriends = 0;
        vm.hasPosts = false;
        vm.noPosts = true;

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
                            var morepost = JSON.stringify({'user_id_a':vm.user.username,'user_id_b':vm.user.username});
                            loadPosts(morepost);
                        });
                }
            }
        }

        function loadCurrentUser() {
            UserService.GetByUsername($rootScope.globals.currentUser.username)
                .then(function (user) {
                    vm.user = user['person'][0];
                    var getpost = JSON.stringify({'user_id_a':user['person'][0].username,'user_id_b':user['person'][0].username});
                    console.log(user['person'][0].id)
                    loadPosts(getpost);
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
                    if(posting['posts'] == 1){
                        vm.areFriends = 1;
                    }
                    else if (posting['posts'] == 0){
                        vm.areFriends = 2;
                    }
                    else{
                        vm.hasPosts = true;
                        vm.noPosts = false;
                        vm.areFriends = 1;    
                    }
                });
        }
    }

})();