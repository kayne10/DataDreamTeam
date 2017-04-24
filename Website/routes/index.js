var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
var Tweets = require('../models/tweets');

/* GET home page. */
// router.get('/', function(req, res, next) {
//   Tweets.find({}, function(err, result){
//     if (err) {
//       console.log(err);
//     } else {
//       res.render('index', {
//         title: 'Data Dream Team',
//         tweets: result
//       });
//     }
//   });
// });

// try to implement pagination
router.get('/', function(req, res, next){
  if (req.query.search) {
    const regex = new RegExp(escapeRegex(req.query.search), 'gi');
    Tweets.find({body: regex}, function(err, result){
      if (err) {
        console.log(err);
      } else {
        if(result.length < 1) {
          var noMatch = 'Sorry, there are no birds who tweeted about this job. Please try again.';
        }
        res.render('index', {
          title: 'Little Bird Told Me',
          tweets: result,
          noMatch: noMatch
        });
      }
    }).limit(300);
  } else {
    // only query a specific amount. DB is too big so use limit() method
    Tweets.find({}, function(err, result){
      if (err) {
        console.log(err);
      } else {
        res.render('index', {
          title: 'Little Bird Told Me',
          tweets: result
        });
      }
    }).limit(20);
  }
});

// GET about page
router.get('/about', function(req, res, next){
  res.render('about', {
    title: 'Little Bird Told Me'
  });
});


module.exports = router;

function escapeRegex(text) {
  return text.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, "\\$&");
};
