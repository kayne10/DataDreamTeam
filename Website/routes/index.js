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

router.get('/', function(req, res, next){
  if (req.query.search) {
    const regex = new RegExp(escapeRegex(req.query.search), 'gi');
    Tweets.find({body: regex}, function(err, result){
      if (err) {
        console.log(err);
      } else {
        res.render('index', {
          title: 'Data Dream Team',
          tweets: result
        });
      }
    });
  } else {
    // only query a specific amount. DB is too big so use $max
    Tweets.find({}, function(err, result){
      if (err) {
        console.log(err);
      } else {
        res.render('index', {
          title: 'Data Dream Team',
          tweets: result
        });
      }
    });
  }
});

module.exports = router;

function escapeRegex(text) {
  return text.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, "\\$&");
};
