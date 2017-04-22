var mongoose = require("mongoose");
var Schema = mongoose.Schema;
var ObjectId = Schema.Types.ObjectId;


var tweetSchema = new Schema({
  id: Number,
  body: String,
  postedTime: Date,
  link: String
});

module.exports = mongoose.model('Tweets', tweetSchema);
