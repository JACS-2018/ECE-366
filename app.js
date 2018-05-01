(function () {
    'use strict';

    angular
        .module('app', ['ngRoute', 'ngCookies'])
        .config(config)
        .run(run);

    config.$inject = ['$routeProvider', '$locationProvider'];
    function config($routeProvider, $locationProvider) {
        $routeProvider
            .when('/', {
                controller: 'HomeController',
                templateUrl: 'home/index.html',
                controllerAs: 'vm'
            })
            .when('/friend', {
                controller: 'FriendController',
                templateUrl: 'friend/friend.html',
                controllerAs: 'vm'
            })
            .when('/friendpage', {
                controller: 'FriendPageController',
                templateUrl: 'friendpage/friendpage.view.html',
                controllerAs: 'vm'
            })
            .when('/profile', {
                controller: 'ProfileController',
                templateUrl: 'profile/profile.html',
                controllerAs: 'vm'
            })
            .when('/request', {
                controller: 'RequestController',
                templateUrl: 'request/requests.html',
                controllerAs: 'vm'
            })
            .when('/request2', {
                controller: 'RequestController',
                templateUrl: 'request/requests2.html',
                controllerAs: 'vm'
            })
            .when('/request3', {
                controller: 'RequestController',
                templateUrl: 'request/requests3.html',
                controllerAs: 'vm'
            })

            .when('/login', {
                controller: 'LoginController',
                templateUrl: 'login/login.view.html',
                controllerAs: 'vm'
            })

            .when('/register', {
                controller: 'RegisterController',
                templateUrl: 'register/register.view.html',
                controllerAs: 'vm'
            })

            .otherwise({ redirectTo: '/login' });
    }

    run.$inject = ['$rootScope', '$location', '$cookies', '$http'];
    function run($rootScope, $location, $cookies, $http) {
        // keep user logged in after page refresh
        $rootScope.globals = $cookies.getObject('globals') || {};
        if ($rootScope.globals.currentUser) {
            $http.defaults.headers.common['Authorization'] = 'Basic ' + $rootScope.globals.currentUser.authdata;
        }

        $rootScope.$on('$locationChangeStart', function (event, next, current) {
            // redirect to login page if not logged in and trying to access a restricted page
            var restrictedPage = $.inArray($location.path(), ['/login', '/register']) === -1;
            var loggedIn = $rootScope.globals.currentUser;
            if (restrictedPage && !loggedIn) {
                $location.path('/login');
            }
        });
    }

})();