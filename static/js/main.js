// main.js
var host = '127.0.0.1:8000';
var app = angular.module('myApp', ['ngGrid']);

app.service('MyService', function($http) {
    var myData = null;

    var promise = $http.get('http://'+host+'/core/video_views/').success(function (data) {
      myData = data;
    });

    return {
      promise:promise,
      setData: function (data) {
          myData = data;
      },
      doStuff: function () {
          return myData;//.getSomeData();
      }
    };
});

app.controller('MyCtrl', function($scope,MyService) {
	MyService.promise.then(function() {
	  	$scope.myData = MyService.doStuff();
	  	console.log(MyService.doStuff());
	  	$scope.$apply()
	});

	$scope.myData = [{id: "", mobile_no: "", video: "", watch_at: null, survey_at: null, has_implemented: null, has_interest: null}];
    $scope.gridOptions = { data: 'myData', 
	    columnDefs: [{field:'id', displayName:'Id'},
		    {field:'mobile_no', displayName:'Contact'},
			{field:'video', displayName:'Video'},
			{field:'watch_at', displayName:'Watch At'},
			{field:'survey_at', displayName:'Survey At'},
			{field:'has_implemented', displayName:'Has Implemented'},
			{field:'has_interest', displayName:'Has Interest'}],
		multiSelect: false
		};
	$scope.survey = function(data) {
		console.log(data)
	}

});