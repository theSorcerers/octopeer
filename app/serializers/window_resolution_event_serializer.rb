class WindowResolutionEventSerializer < ActiveModel::Serializer
  attributes :id, :width, :height, :created_at
  has_one :session
end
