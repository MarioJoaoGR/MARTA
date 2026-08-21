require "rspec"
require "carteira"

RSpec.describe Carteira do
  # Scenario 1: Valid inputs (Happy Path)
  it "should return a resumo with the current saldo when initialized with minimal args" do
    carteira = Carteira.new
    expect(carteira.resumo).to eq("Saldo actual: #{0}")
  end

  # Scenario 2: Edge cases (e.g., nil, empty arrays, boundary values)
  it "should raise an error when initialized with invalid args" do
    expect { Carteira.new(nil) }.to raise_error(ArgumentError)
  end

  # Scenario 3: Invalid inputs / error handling (e.g., raising an error)
  it "should return a resumo with the current saldo when initialized with valid args" do
    carteira = Carteira.new
    allow(carteira).to receive(:saldo).and_return(100)
    expect(carteira.resumo).to eq("Saldo actual: #{100}")
  end
end
