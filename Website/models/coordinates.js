// var mongoose = require("mongoose");
// var Schema = mongoose.Schema;
// var ObjectId = Schema.Types.ObjectId;
//
//
// var coordinateSchema = new Schema({
//   type: {type:String, required: true},
//   coordinates: [Number]
//   // body: {type: String, required: true}
// });
//
// module.exports = mongoose.model('Coordinates', coordinateSchema);

// tried importing geojson npm library
var GeoJSON = require('mongoose-geojson-schema');
var mongoose = require('mongoose');

var coordinateSchema = mongoose.Schema({
  feature: mongoose.Schema.Types.Feature,
  geometry: mongoose.Schema.Types.Geometry
});
