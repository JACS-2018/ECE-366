(function () {
    'use strict';

    angular
        .module('app')
        .controller('FriendPageController', FriendPageController);

    FriendPageController.$inject = ['UserService', '$rootScope','$location', '$scope'];
    function FriendPageController(UserService, $rootScope, $location) {
        var vm = this;

        vm.user = null;
        vm.allUsers = [];
        vm.deleteUser = deleteUser;
        vm.allPosts= [];
        vm.post = post;
        vm.areFriends = 0;
        vm.hasPosts = false;
        vm.noPosts = true;
        vm.friendUser = $location.url().split('#')[1];
        vm.friendrequestsuccess = friendrequestsuccess;
        vm.friendrequestsuccesser = null
        vm.canceller = null;
        vm.requestings = null;
        vm.cancel = cancel;
        vm.getUser = getUser;

        initController();


        function initController() {
            loadCurrentUser();
            loadAllUsers();
            getUser();
            console.log($location.url().split('#')[1]);
            console.log(vm.allPosts);
            console.log(vm.requestings);
        }

        function friendrequestsuccess(){
            var morefriend = JSON.stringify({'user_id_a':vm.user.username,'user_id_b':$location.url().split('#')[1]});
            UserService.MakeFriend(morefriend)
                .then(function (response) {
                    vm.friendrequestsuccesser = response['success'];
                    console.log(response);
                    requestexists(vm.user.username);
                });
        }

        function requestexists(current){
            var morefriend = JSON.stringify({'user_id_a':current,'user_id_b':$location.url().split('#')[1]});
            console.log(morefriend);
            UserService.RequestExists(morefriend)
                .then(function (response) {
                    vm.requestings = response['exists'];
                    console.log(vm.requestings);
                });
        }

        function cancel(){
            var morecancel = JSON.stringify({'user_id_a':vm.user.username,'user_id_b':$location.url().split('#')[1], 'status':0});
            UserService.ConfirmFriend(morecancel)
                .then(function (response) {
                    vm.canceller = response['result'];
                    console.log(vm.canceller);
                    requestexists(vm.user.username);
                });
        }

        function post(content) {
            if (typeof content !== 'undefined'){
                if(content.length !== 0){
                    content = content.trim();
                    var newpost = JSON.stringify({'user_id_a':vm.user.username,'user_id_b':$location.url().split('#')[1], 'content':content});
                    console.log(content);
                     UserService.MakePost(newpost)
                        .then(function (posting) {
                            console.log(posting);
                            console.log(vm.user.username);
                            var morepost = JSON.stringify({'user_id_a':vm.user.username,'user_id_b':$location.url().split('#')[1]});
                            loadPosts(morepost);
                        });
                }
            }
        }

        function loadCurrentUser() {
            UserService.GetByUsername($rootScope.globals.currentUser.username)
                .then(function (user) {
                    vm.user = user['person'][0];
                    console.log(user['person'][0].id)
                    var getpost = JSON.stringify({'user_id_a':user['person'][0].username,'user_id_b':$location.url().split('#')[1]});
                    loadPosts(getpost);
                    requestexists(user['person'][0].username);
                });
        }

        function getUser() {
            UserService.GetByUsername(vm.friendUser)
                .then(function (user) {
                    vm.getUser = user['person'][0];
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