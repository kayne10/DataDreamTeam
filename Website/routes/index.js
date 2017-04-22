var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
var Tweets = require('../models/tweets');

/* GET home page. */
router.get('/', function(req, res, next) {
  Tweets.find({}, function(err, result){
    res.render('index', {
      title: 'Data Dream Team',
      tweets: result
    });
  });
});

module.exports = router;
