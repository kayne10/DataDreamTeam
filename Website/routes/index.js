var express = require('express');
var router = express.Router();

// Create Cassandra Connection
const cassandra = require('cassandra-driver');
const client = new cassandra.Client({ contactPoints: ['127.0.0.1:9042'] });
client.connect(function (err) {
  if (err) throw err;
});


/* GET home page. */
router.get('/', function(req, res, next) {
  const query = "SELECT text, url, created_at FROM tweets";
  client.execute(query, function (err, result) {
    var tweet = result;
    console.log(tweet);
    res.render('index', {
      title: 'Express',
      tweet: tweet
     });
  });
});

module.exports = router;
