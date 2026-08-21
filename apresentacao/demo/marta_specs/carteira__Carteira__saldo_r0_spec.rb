require "rspec"
require "carteira"

RSpec.describe Carteira do
  context "when @mov is set" do
    it "should return the total of movements for a valid instance" do
      cart = Carteira.new
      mov = Movimento.new
      allow(mov).to receive(:total).and_return(100)
      cart.instance_variable_set(:@mov, mov)
      expect(cart.saldo).to eq(100)
    end
  end


  context "when invalid argument is passed to initialize" do
    it "should raise an ArgumentError if the argument passed to initialize is invalid" do
      expect { Carteira.new("invalid_argument") }.to raise_error(ArgumentError)
    end
  end
end
