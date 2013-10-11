%% Copyright
-module(hello_world).
-author("nikh0881").


%erl command used to compile and run this program%
%$erl -compile hello_world.erl %
%erl -noshell -s hello_world start -s init stop%


%% API
-export([start/0]).
start() ->
  io:fwrite("Hello, world!\n").
