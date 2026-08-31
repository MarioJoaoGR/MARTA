require "formatador/table"
RSpec.describe Formatador do
  describe "#calculate_datum" do
    it "retrieves a value using a direct key in the hash" do
      hash = {'key' => 'value'}
      header = 'key'
      expect(subject.send(:calculate_datum, header, hash)).to eq('value')
    end

    it "retrieves a value using a dot-separated path in the hash" do
      hash = {'a' => {'b' => {'c' => 'value'}}}
      header = 'a.b.c'
      expect(subject.send(:calculate_datum, header, hash)).to eq('value')
    end

    it "handles missing key gracefully" do
      hash = {'existingKey' => 'value'}
      header = 'nonExistentKey'
      expect(subject.send(:calculate_datum, header, hash)).to eq('')
    end
  end
end
