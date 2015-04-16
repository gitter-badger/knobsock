'use strict';

var KnobSock = angular.module('KnobSock', ['ngRoute']);

KnobSock.factory('guestService', function($rootScope, $http, $q, $log) {
  $rootScope.status = 'Retrieving data...';
  var deferred = $q.defer();
  $http.get('rest/query')
  .success(function(data, status, headers, config) {
    $rootScope.guests = data;
    deferred.resolve();
    $rootScope.status = '';
  });
  return deferred.promise;
});

KnobSock.config(function($routeProvider) {
  $routeProvider.when('/', {
    controller: 'SplashCtrl',
    templateUrl: '/partials/splash.html',
  });
  $routeProvider.when('/dashboard', {
    controller: 'DashCtrl',
    templateUrl: '/partials/dashboard.html',
  });
  $routeProvider.otherwise({
    redirectTo: '/'
  });
});

KnobSock.controller('SplashCtrl', function($scope, $rootScope, $log, $http, $routeParams, $location, $route) {

});

KnobSock.controller('DashCtrl', function($scope, $rootScope, $log, $http, $routeParams, $location, $route) {

  $scope.submitInsert = function() {
    var guest = {
      first: $scope.first,
      last: $scope.last, 
    };
    $rootScope.status = 'Creating...';
    $http.post('/rest/insert', guest)
    .success(function(data, status, headers, config) {
      $rootScope.guests.push(data);
      $rootScope.status = '';
    });
    $location.path('/');
  }
});

