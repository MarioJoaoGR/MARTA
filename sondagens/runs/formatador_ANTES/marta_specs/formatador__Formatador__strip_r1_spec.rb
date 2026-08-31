require "formatador"

RSpec.describe Formatador do
  it "handles valid inputs correctly" do
    formatador = Formatador.new
    expect(formatador.display("Hello, World!")).to eq nil
  end

  it "handles edge cases such as nil and empty strings gracefully" do
    formatador = Formatador.new
    expect { formatador.display(nil) }.not_to raise_error
    expect { formatador.display("") }.not_to raise_error
  end

end
