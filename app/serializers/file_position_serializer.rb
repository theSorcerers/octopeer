class FilePositionSerializer < ActiveModel::Serializer
  attributes :id, :commit_hash, :filename, :line_number
  has_one :semantic_event
end
