require "formatador"

RSpec.describe Formatador do
  describe "#redisplay_line" do
    it "should handle valid input string and width" do
      formatador = Formatador.new
      expect { formatador.redisplay_line("Hello, World!", 80) }.not_to raise_error
    end



    it "should raise an error for invalid width" do
      formatador = Formatador.new
      expect { formatador.redisplay_line("Hello, World!", -1) }.to raise_error(ArgumentError)
    end
  end
end
