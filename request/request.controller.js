(function () {
    'use strict';

    angular
        .module('app')
        .controller('RequestController', RequestController);

    RequestController.$inject = ['UserService', '$rootScope','$location'];
    function RequestController(UserService, $rootScope, $location) {
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
        vm.requestings = null;
        vm.allRequests = [];
        vm.allRequestsIncoming = [];
        vm.AllFriends = [];
        vm.allRequestsLen = 0;
        vm.allRequestsIncomingLen = 0;
        vm.AllFriendsLen = 0;

        initController();


        function initController() {
            loadCurrentUser();
            loadAllUsers();
        }

        function getallRequestedRequests(current){
            UserService.GetRequestedFriends(current)
                .then(function (users) {
                    vm.allRequests = users['person'];
                    console.log("Outgoing");
                    console.log(vm.allRequests.length);
                    if (vm.allRequests.length !== 0){
                        vm.allRequestsLen = 1;
                    }
                    console.log(vm.allRequestsLen);
                });
        }

        function getallIncomingRequests(current){
            UserService.GetIncomingFriends(current)
                .then(function (users) {
                    vm.allRequestsIncoming = users['person'];
                    console.log("Incoming");
                    console.log(vm.allRequestsIncoming.length);
                    if (vm.allRequestsIncoming.length !== 0){
                        vm.allRequestsIncomingLen =  1;
                    }
                    console.log(vm.allRequestsIncomingLen);
                });
        }

        function getallFriendships(current){
            UserService.GetAllFriends(current)
                .then(function (users) {
                    vm.AllFriends = users['person'];
                    console.log("All");
                    console.log(vm.AllFriends.length);
                    if (vm.AllFriends.length !== 0){
                        vm.AllFriendsLen = 1;
                    }
                    console.log(vm.AllFriendsLen);
                });
        }

        function friendrequestsuccess(){
            var morefriend = JSON.stringify({'user_id_a':vm.user.username,'user_id_b':$location.url().split('#')[1]});
            UserService.MakeFriend(morefriend)
                .then(function (response) {
                    vm.friendrequestsuccess = response['success'];
                    requestexists(vm.user.username);
                });
        }

        function post(content) {
            if (typeof content !== 'undefined'){
                if(content.length !== 0){
                    content = content.trim();
                    var newpost = JSON.stringify({'user_id_a':vm.user.username,'user_id_b':$location.url().split('#')[1], 'content':content});
                     UserService.MakePost(newpost)
                        .then(function (posting) {
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
                    var getpost = JSON.stringify({'user_id_a':user['person'][0].username,'user_id_b':$location.url().split('#')[1]});
                    getallRequestedRequests(user['person'][0].username);
                    getallIncomingRequests(user['person'][0].username);
                    getallFriendships(user['person'][0].username);
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