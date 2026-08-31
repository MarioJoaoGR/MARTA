require "formatador"

RSpec.describe Formatador do
  describe "#new_line" do
    it "prints a new line when called" do
      expect { Formatador.new_line }.to output("\n").to_stdout
    end
  end
end
