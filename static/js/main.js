// main.js
var host = '127.0.0.1:8000';
var app = angular.module('myApp', ['ngGrid']);

app.service('MyService', function($http) {
    var myData = null;

    var promise = $http.get('/core/video_views/').success(function (data) {
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

app.controller('MyCtrl', function($scope,$http,MyService) {
	MyService.promise.then(function() {
	  	$scope.myData = MyService.doStuff();
	  	console.log(MyService.doStuff());
	  	$scope.$apply()
	});
	$scope.selectedItems = []
	$scope.myData = [{id: "", mobile_no: "", video: "", watch_at: null, survey_at: null, has_implemented: null, has_interest: null}];
    $scope.gridOptions = { data: 'myData', 
	    columnDefs: [{field:'id', displayName:'Id'},
		    {field:'mobile_no', displayName:'Contact'},
			{field:'video', displayName:'Video'},
			//{field:'watch_at', displayName:'Watched At'},
			{field:'survey_at', displayName:'Survey At'},
			{field:'has_implemented', displayName:'Has Implemented'},
			{field:'has_interest', displayName:'Has Interest'},
			{field:'recording_url', displayName:'Feedback', cellTemplate: '<div ng-switch="!!row.entity[col.field]"><a class="link" href="{{row.entity[col.field]}}" target="_new" ng-switch-when="true">Listen</a></div>'}],
		multiSelect: false,
		keepLastSelected: true,
		jqueryUITheme: true,
		selectedItems: $scope.selectedItems
	};
	$scope.$on('ngGridEventData', function(){
        $scope.gridOptions.selectRow(0, true);
    });
	$scope.survey = function(data) {
		var obj = $scope.selectedItems[0]
		if(obj) {
			$http.get('/ivr/survey/video_id/'+obj.video+'/mobile_no/'+obj.mobile_no+'/')
			.success(function(data) {
				console.log(data);
				document.getElementById("notification").innerHTML = JSON.toString(data.Call)
			})
			.error(function(data) {
				document.getElementById("notification").innerHTML = data.RestException.Message
			})
		}
	}

});