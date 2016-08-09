class MouseClickEventSerializer < ActiveModel::Serializer
  attributes :id, :created_at
  has_one :session
end
