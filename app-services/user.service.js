(function () {
    'use strict';

    angular
        .module('app')
        .factory('UserService', UserService);

    UserService.$inject = ['$http'];
    function UserService($http) {
        var service = {};

        service.GetAll = GetAll;
        service.GetById = GetById;
        service.GetByUsername = GetByUsername;
        service.Create = Create;
        service.Update = Update;
        service.Delete = Delete;
        service.MakePost = MakePost;
        service.GetPostById = GetPostById;
        service.GetAllFriends = GetAllFriends;
        service.GetRequestedFriends = GetRequestedFriends;
        service.GetIncomingFriends = GetIncomingFriends;
        service.MakeFriend = MakeFriend;
        service.ConfirmFriend = ConfirmFriend;

        return service;

        function GetAll() {
            return $http.get('http://127.0.0.1:5000/api/users').then(handleSuccess, handleError('Error getting all users'));
        }

        function GetById(id) {
            return $http.get('http://127.0.0.1:5000/api/users/' + id).then(handleSuccess, handleError('Error getting user by id'));
        }

        function GetByUsername(username) {
            return $http.get('http://127.0.0.1:5000/api/users/' + username).then(handleSuccess, handleError('Error getting user by username'));
        }

        function Create(user) {
            return $http.post('http://127.0.0.1:5000/api/users', user).then(handleSuccess, handleError('Error creating user'));
        }

        function Update(user) {
            return $http.put('http://127.0.0.1:5000/api/users/' + user.id, user).then(handleSuccess, handleError('Error updating user'));
        }

        function Delete(id) {
            return $http.delete('http://127.0.0.1:5000/api/users/' + id).then(handleSuccess, handleError('Error deleting user'));
        }

        function MakePost(post){
            return $http.post('http://127.0.0.1:5000/api/posts', post).then(handleSuccess, handleError('Error making post'));
        }

        function GetPostById(id) {
            return $http.get('http://127.0.0.1:5000/api/posts/' + id).then(handleSuccess, handleError('Error getting post by id'));
        }

        function GetAllFriends(id) {
            return $http.get('http://127.0.0.1:5000/api/friendships/' + id).then(handleSuccess, handleError('Error getting friends by id'));
        }

        function GetRequestedFriends(id) {
            return $http.get('http://127.0.0.1:5000/api/friendships/awaited/' + id).then(handleSuccess, handleError('Error getting requested friends by id'));
        }

        function GetIncomingFriends(id) {
            return $http.get('http://127.0.0.1:5000/api/friendships/confirm/' + id).then(handleSuccess, handleError('Error getting incoming friends by id'));
        }

        function MakeFriend(friend){
            return $http.post('http://127.0.0.1:5000/api/friendships/add', friend).then(handleSuccess, handleError('Error making friend'));
        }

        function ConfirmFriend(friend){
            return $http.post('http://127.0.0.1:5000/api/friendships/confirming', friend).then(handleSuccess, handleError('Error confirming friend'));
        }

        function RequestExists(id) {
            return $http.get('http://127.0.0.1:5000/api/friendships/exists/' + id).then(handleSuccess, handleError('Error getting request'));
        }
        // private functions

        function handleSuccess(res) {
            console.log(res)
            return res.data;
        }

        function handleError(error) {
            return function () {
                return { success: false, message: error };
            };
        }
    }

})();
