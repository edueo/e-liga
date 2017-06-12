'use strict'

const Hapi = require('hapi');
const mongoose = require('mongoose');

var playerSchema = mongoose.Schema({
  name : String,
  aka: String
});

var Player = mongoose.model('Player', playerSchema);


mongoose.connect('mongodb://eliga_user:pepejatireiavela@ds143151.mlab.com:43151/eliga');
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
    console.log('estamos dentro');
});

const server = new Hapi.Server();

server.connection({ port: 3000, host: 'localhost' });

server.route({
  method : 'GET',
  path : '/',
  handler: function(request, reply) {
    reply('Hello, world');
  }
});

server.route({
  method: 'GET',
  path : '/{name}',
  handler: function(request, reply) {
    reply('Hello,' + encodeURIComponent(request.params.name) + '!' );
  }

});

server.route({
  method: 'POST',
  path: '/players',
  handler: function(request, reply) {
    console.log(request.payload)
    var player1 = new Player(request.payload.attributes);

    player1.save(function (err, player1) {
      if(err) return console.error(err);

      var players = Player.find();
      reply(players)
      .code(201)
      .type('application/vnd.api+json');

      console.log('Jogador Salvo!!!');

    });

     }
});

server.start( (err) => {

  if(err) {
    throw err;
  }

  console.log(`Server running at:${server.info.uri}`);

});
