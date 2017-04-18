var express = require('express');
var router = express.Router();

// Create Cassandra Connection
var cassandra = require('cassandra-driver');
var client = new cassandra.Client({ contactPoints: ['localhost'] });
client.connect(function (err) {
  if (err) throw err;
});


/* GET home page. */
router.get('/', function(req, res, next) {
  const query = 'SELECT text, url, created_at FROM ddt.tweets';
  client.execute(query, function (err, result) {
    if (err) return next(err);
    var tweets = result.rows;
    // console.log(tweets);
    res.render('index', {
      title: 'Data Dream Team',
      tweets: tweets
     });
  });
});

module.exports = router;
