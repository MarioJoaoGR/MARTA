require "formatador"

RSpec.describe Formatador do
  it "handles valid inputs correctly" do
    formatador = Formatador.new
    expect(formatador.display("Hello, World!")).to eq nil
    expect(formatador.new_line).to eq nil
  end

end
