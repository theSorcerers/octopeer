class SemanticEventSerializer < ActiveModel::Serializer
  attributes :id, :created_at
  has_one :session
  has_one :event_type
  has_one :element_type
end
