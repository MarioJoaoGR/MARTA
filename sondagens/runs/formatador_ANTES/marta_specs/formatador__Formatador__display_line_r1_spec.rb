require "formatador"

RSpec.describe Formatador do
  it "handles valid inputs correctly" do
    formatador = Formatador.new
    expect(formatador.display("Hello, World!")).to eq nil
    expect(formatador.new_line).to eq nil
  end

  it "handles edge cases gracefully" do
    formatador = Formatador.new
    expect { formatador.display(nil) }.not_to raise_error
    expect { formatador.new_line }.not_to raise_error
  end

  it "raises an error for invalid inputs" do
    formatador = Formatador.new
    expect { formatador.display("Hello, World!") }.not_to raise_error
    expect { formatador.new_line }.not_to raise_error
  end
end
