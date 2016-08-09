class MouseScrollEventSerializer < ActiveModel::Serializer
  attributes :id, :viewport_x, :viewport_y, :created_at
  has_one :session
end
