(function () {
    'use strict';

    angular
        .module('app')
        .controller('ProfileController', ProfileController);

    ProfileController.$inject = ['UserService', '$rootScope','$location'];
    function ProfileController(UserService, $rootScope) {
        var vm = this;

        vm.user = null;
        vm.allUsers = [];
        vm.deleteUser = deleteUser;
        vm.update = update;
  

        initController();

        function initController() {
            loadCurrentUser();
            loadAllUsers();
        }

        function update(desc, email, bday){
            var descval = 0;
            var emailval = 0;
            var bdayval = 0;
            if (typeof desc !== 'undefined'){
                if(desc.length !== 0){
                    descval=desc;
                }
            }
            if (typeof email !== 'undefined'){
                if(email.length !== 0){
                   emailval=email;
                }
            }
            if (typeof bday !== 'undefined'){
                if(bday.length !== 0){
                    bdayval=bday;
                }
            }
            var newuser = JSON.stringify({'username':vm.user.username,'desc':descval,'email':emailval, 'bday':bdayval});
            UserService.CreateTemp(newuser)
                .then(function (user) {
                    console.log(user);
                    loadCurrentUser();
                });
        }

        function loadCurrentUser() {
            UserService.GetByUsername($rootScope.globals.currentUser.username)
                .then(function (user) {
                    console.log(user['person'][0]);
                    vm.user = user['person'][0];
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