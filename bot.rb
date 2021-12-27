require 'telegram_bot'
require './config.rb'
token = Config::TOKEN
bot = TelegramBot.new(token: token)

bot.get_updates(fail_silently: true) do |message|
    puts "@#{message.from.username}: #{message.text}"
    command = message.get_command_for(bot)
  
    message.reply do |reply|
      case command
      when /start/i
        reply.text = "All I can do is say hello. Try the /greet command."
      when /greet/i
        reply.text = "Hello, #{message.from.first_name}. 🤖"
      else
        reply.text = "I have no idea what #{command.inspect} means."
      end
      puts "sending #{reply.text.inspect} to @#{message.from.username}"
      reply.send_with(bot)
    end
  end
