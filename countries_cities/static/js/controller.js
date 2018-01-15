var app = angular.module('ccApp', []);
app.controller('ccController', function($scope, $http) {

    $http({method: 'GET', url: 'http://localhost:5000/countries'}).
            then(function(response) {
                $scope.countries = response.data;
                console.log(response.data)
            }, function(response) {
                console.log(response, 'error')
          });
    $scope.clickHandler = function(id){
        $http({method: 'GET', url: 'http://localhost:5000/cities/'+id}).
            then(function(response) {
                $scope.cities = response.data;
                console.log(response.data)
            }, function(response) {
                console.log(response, 'error')
          });
    };
});