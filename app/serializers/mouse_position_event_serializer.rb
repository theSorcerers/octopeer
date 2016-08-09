class MousePositionEventSerializer < ActiveModel::Serializer
  attributes :id, :position_x, :position_y, :viewport_x, :viewport_y, :created_at
  has_one :session
end
