var mongoose = require('mongoose');
var _ = require('underscore');
var Tweets = require('../models/tweets');
var Coordinates = require('../models/coordinates');

mongoose.Promise = require('bluebird');
mongoose.connect('localhost:27017/ddt');


Tweets.find({}, function(err, result){
  if (err) throw err;
  var tweets = result;
  var coordinates = _.compact(_.map(tweets, function(myTweetItem) {
    // console.log('*************************');
    // console.log(myTweetItem.get('geo',));
    // console.log('*************************');
    var geoCoordinates = myTweetItem.get('geo');
    // var info = myTweetItem.get('body');
    return geoCoordinates;
    // return {"tweet":info,"geometry":geoCoordinates};
  }));
  console.log(coordinates);
  var done = 0;
  for (var i = 0; i < coordinates.length; i++) {
    var tmp = new Coordinates({
      type: coordinates[i].type,
      coordinates: coordinates[i].coordinates,
      // body: coordinates[i].tweet
    });
    tmp.save(function(err, data){
      done++;
      console.log('Coordinate Saved');
      if (done === coordinates.length) {
        exit();
      }
    });
  }
  // exit();
});

function exit() {
  mongoose.disconnect();
}
